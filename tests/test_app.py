import pytest
import json
from app.app import create_app


@pytest.fixture
def app():
    """Create and configure a test instance of the app."""
    app = create_app({'TESTING': True})
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


class TestHealthCheck:
    """Test health check endpoint"""
    
    def test_health_endpoint(self, client):
        """Test that health endpoint returns 200"""
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'ok'


class TestHomePage:
    """Test home page functionality"""
    
    def test_index_endpoint(self, client):
        """Test that index endpoint returns API info"""
        response = client.get('/')
        assert response.status_code == 200
        data = response.get_json()
        assert 'message' in data
        assert 'ACEestFitness' in data['message']
    
    def test_ui_endpoint(self, client):
        """Test that UI endpoint returns HTML"""
        response = client.get('/ui')
        assert response.status_code == 200
        assert b'ACEest' in response.data


class TestAddWorkout:
    """Test add workout functionality"""
    
    def test_add_workout_success(self, client):
        """Test adding a valid workout"""
        response = client.post('/workouts',
            json={
                'category': 'Workout',
                'workout': 'Push-ups',
                'duration': 30
            },
            content_type='application/json'
        )
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == 'Workout added'
        assert data['entry']['exercise'] == 'Push-ups'
        assert data['entry']['duration'] == 30
    
    def test_add_workout_with_warmup_category(self, client):
        """Test adding workout in Warm-up category"""
        response = client.post('/workouts',
            json={
                'category': 'Warm-up',
                'workout': 'Stretching',
                'duration': 10
            },
            content_type='application/json'
        )
        assert response.status_code == 201
        data = response.get_json()
        assert data['category'] == 'Warm-up'
    
    def test_add_workout_with_cooldown_category(self, client):
        """Test adding workout in Cool-down category"""
        response = client.post('/workouts',
            json={
                'category': 'Cool-down',
                'workout': 'Walking',
                'duration': 5
            },
            content_type='application/json'
        )
        assert response.status_code == 201
        data = response.get_json()
        assert data['category'] == 'Cool-down'
    
    def test_add_workout_missing_workout_field(self, client):
        """Test adding workout with missing workout field"""
        response = client.post('/workouts',
            json={
                'category': 'Workout',
                'duration': 30
            },
            content_type='application/json'
        )
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
    
    def test_add_workout_missing_duration(self, client):
        """Test adding workout with missing duration"""
        response = client.post('/workouts',
            json={
                'category': 'Workout',
                'workout': 'Push-ups'
            },
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_add_workout_invalid_duration_string(self, client):
        """Test adding workout with invalid duration (string)"""
        response = client.post('/workouts',
            json={
                'category': 'Workout',
                'workout': 'Push-ups',
                'duration': 'invalid'
            },
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_add_workout_negative_duration(self, client):
        """Test adding workout with negative duration"""
        response = client.post('/workouts',
            json={
                'category': 'Workout',
                'workout': 'Push-ups',
                'duration': -10
            },
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_add_workout_zero_duration(self, client):
        """Test adding workout with zero duration"""
        response = client.post('/workouts',
            json={
                'category': 'Workout',
                'workout': 'Push-ups',
                'duration': 0
            },
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_add_workout_invalid_category(self, client):
        """Test adding workout with invalid category"""
        response = client.post('/workouts',
            json={
                'category': 'InvalidCategory',
                'workout': 'Push-ups',
                'duration': 30
            },
            content_type='application/json'
        )
        assert response.status_code == 400
        data = response.get_json()
        assert 'Invalid category' in data['error']
    
    def test_add_workout_wrong_content_type(self, client):
        """Test adding workout with wrong content type"""
        response = client.post('/workouts',
            data='not json',
            content_type='text/plain'
        )
        assert response.status_code == 415
        data = response.get_json()
        assert 'application/json' in data['error']


class TestListWorkouts:
    """Test list workouts functionality"""
    
    def test_list_workouts_empty(self, client):
        """Test listing workouts when none exist"""
        response = client.get('/workouts')
        assert response.status_code == 200
        data = response.get_json()
        assert data['count'] == 0
        assert data['workouts'] == []
    
    def test_list_workouts_with_data(self, client):
        """Test listing workouts after adding data"""
        # Add multiple workouts
        workouts = [
            {'category': 'Warm-up', 'workout': 'Stretching', 'duration': 10},
            {'category': 'Workout', 'workout': 'Squats', 'duration': 20},
            {'category': 'Cool-down', 'workout': 'Walking', 'duration': 5}
        ]
        
        for workout_data in workouts:
            client.post('/workouts', json=workout_data, content_type='application/json')
        
        # List all workouts
        response = client.get('/workouts')
        assert response.status_code == 200
        data = response.get_json()
        assert data['count'] == 3
        assert len(data['workouts']) == 3
        
        # Verify categories are present
        categories = [w['category'] for w in data['workouts']]
        assert 'Warm-up' in categories
        assert 'Workout' in categories
        assert 'Cool-down' in categories


class TestSummary:
    """Test summary functionality"""
    
    def test_summary_empty(self, client):
        """Test summary when no workouts exist"""
        response = client.get('/summary')
        assert response.status_code == 200
        data = response.get_json()
        assert data['total_time'] == 0
    
    def test_summary_with_workouts(self, client):
        """Test summary after adding workouts"""
        # Add workouts
        client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Running',
            'duration': 30
        }, content_type='application/json')
        
        client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Cycling',
            'duration': 45
        }, content_type='application/json')
        
        # Get summary
        response = client.get('/summary')
        assert response.status_code == 200
        data = response.get_json()
        assert data['total_time'] == 75
        assert 'motivation' in data
    
    def test_summary_motivation_good_start(self, client):
        """Test motivation message for < 30 minutes"""
        client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Walking',
            'duration': 20
        }, content_type='application/json')
        
        response = client.get('/summary')
        data = response.get_json()
        assert 'Good start' in data['motivation']
    
    def test_summary_motivation_nice_effort(self, client):
        """Test motivation message for 30-60 minutes"""
        client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Running',
            'duration': 45
        }, content_type='application/json')
        
        response = client.get('/summary')
        data = response.get_json()
        assert 'Nice effort' in data['motivation']
    
    def test_summary_motivation_excellent(self, client):
        """Test motivation message for > 60 minutes"""
        client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Marathon',
            'duration': 90
        }, content_type='application/json')
        
        response = client.get('/summary')
        data = response.get_json()
        assert 'Excellent' in data['motivation']
    
    def test_summary_by_category(self, client):
        """Test that summary includes breakdown by category"""
        # Add workouts to different categories
        client.post('/workouts', json={
            'category': 'Warm-up',
            'workout': 'Stretching',
            'duration': 10
        }, content_type='application/json')
        
        client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Squats',
            'duration': 30
        }, content_type='application/json')
        
        response = client.get('/summary')
        data = response.get_json()
        assert 'by_category' in data
        assert 'Warm-up' in data['by_category']
        assert 'Workout' in data['by_category']


class TestIntegration:
    """Integration tests for complete workflows"""
    
    def test_full_workout_session_workflow(self, client):
        """Test complete workout session from start to finish"""
        # 1. Check initial state
        response = client.get('/workouts')
        assert response.get_json()['count'] == 0
        
        # 2. Add warm-up
        response = client.post('/workouts', json={
            'category': 'Warm-up',
            'workout': 'Jogging',
            'duration': 5
        }, content_type='application/json')
        assert response.status_code == 201
        
        # 3. Add main workout
        response = client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Weight Training',
            'duration': 45
        }, content_type='application/json')
        assert response.status_code == 201
        
        # 4. Add cool-down
        response = client.post('/workouts', json={
            'category': 'Cool-down',
            'workout': 'Stretching',
            'duration': 10
        }, content_type='application/json')
        assert response.status_code == 201
        
        # 5. Verify all workouts are recorded
        response = client.get('/workouts')
        data = response.get_json()
        assert data['count'] == 3
        
        # 6. Check summary
        response = client.get('/summary')
        data = response.get_json()
        assert data['total_time'] == 60
        assert 'Excellent' in data['motivation']
    
    def test_multiple_sessions_same_category(self, client):
        """Test adding multiple workouts to the same category"""
        exercises = ['Push-ups', 'Pull-ups', 'Squats', 'Lunges']
        
        for exercise in exercises:
            response = client.post('/workouts', json={
                'category': 'Workout',
                'workout': exercise,
                'duration': 15
            }, content_type='application/json')
            assert response.status_code == 201
        
        response = client.get('/workouts')
        data = response.get_json()
        assert data['count'] == 4
        
        workout_names = [w['exercise'] for w in data['workouts']]
        for exercise in exercises:
            assert exercise in workout_names
    
    def test_api_resilience_to_bad_requests(self, client):
        """Test that API handles various bad requests gracefully"""
        bad_requests = [
            ({}, 400),  # Empty body
            ({'workout': 'Test'}, 400),  # Missing duration
            ({'duration': 30}, 400),  # Missing workout
            ({'category': 'Invalid', 'workout': 'Test', 'duration': 30}, 400),  # Invalid category
            ({'workout': '', 'duration': 30}, 400),  # Empty workout name
        ]
        
        for payload, expected_status in bad_requests:
            response = client.post('/workouts', json=payload, content_type='application/json')
            assert response.status_code == expected_status


class TestErrorHandling:
    """Test error handling and edge cases"""
    
    def test_empty_workout_name(self, client):
        """Test that empty workout names are rejected"""
        response = client.post('/workouts', json={
            'category': 'Workout',
            'workout': '   ',  # Only whitespace
            'duration': 30
        }, content_type='application/json')
        assert response.status_code == 400
    
    def test_very_large_duration(self, client):
        """Test handling of very large duration values"""
        response = client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Marathon',
            'duration': 999999
        }, content_type='application/json')
        # Should accept large but valid numbers
        assert response.status_code == 201
    
    def test_float_duration(self, client):
        """Test that float durations are handled"""
        response = client.post('/workouts', json={
            'category': 'Workout',
            'workout': 'Running',
            'duration': 30.5
        }, content_type='application/json')
        # Should convert to int and accept
        assert response.status_code in [201, 400]  # Either accepts or rejects floats


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
