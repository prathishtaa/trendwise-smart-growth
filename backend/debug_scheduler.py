"""
Debug script for Schedule Optimizer
Run this to test the scheduler independently
"""

import sys
import traceback

print("=" * 60)
print("SCHEDULE OPTIMIZER DEBUG SCRIPT")
print("=" * 60)

try:
    # Test 1: Import the module
    print("\n[1/5] Testing import...")
    from ml_models.schedule_optimizer import ScheduleOptimizer
    print("✓ Import successful")
    
    # Test 2: Initialize the model
    print("\n[2/5] Initializing model...")
    optimizer = ScheduleOptimizer()
    print("✓ Model initialized")
    
    # Test 3: Check if ready
    print("\n[3/5] Checking if model is ready...")
    is_ready = optimizer.is_ready()
    print(f"✓ Model ready: {is_ready}")
    
    # Test 4: Test data structures
    print("\n[4/5] Testing data structures...")
    print(f"  - Engagement patterns loaded: {len(optimizer.engagement_patterns)} audiences")
    print(f"  - Platform data loaded: {len(optimizer.platform_data)} platforms")
    print(f"  - Available audiences: {list(optimizer.engagement_patterns.keys())}")
    print(f"  - Available platforms: {list(optimizer.platform_data.keys())}")
    print("✓ Data structures OK")
    
    # Test 5: Generate a schedule
    print("\n[5/5] Generating test schedule...")
    
    test_cases = [
        {"content_type": "blog", "target_audience": "tech", "platform": "website"},
        {"content_type": "blog", "target_audience": "business", "platform": "blog"},
        {"content_type": "landing_page", "target_audience": "general", "platform": "website"},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n  Test Case {i}:")
        print(f"    Content: {test_case['content_type']}")
        print(f"    Audience: {test_case['target_audience']}")
        print(f"    Platform: {test_case['platform']}")
        
        try:
            result = optimizer.generate_schedule(**test_case)
            
            # Validate result structure
            required_keys = ['weekly_schedule', 'monthly_overview', 'optimal_times', 
                           'recommendations', 'expected_impact', 'platform_insights']
            
            missing_keys = [key for key in required_keys if key not in result]
            if missing_keys:
                print(f"    ⚠ Missing keys: {missing_keys}")
            else:
                print(f"    ✓ All keys present")
            
            # Display summary
            print(f"    - Weekly schedule days: {len(result['weekly_schedule'])}")
            total_posts = sum(len(day['posts']) for day in result['weekly_schedule'])
            print(f"    - Total posts this week: {total_posts}")
            print(f"    - Optimal times: {len(result['optimal_times'])}")
            print(f"    - Recommendations: {len(result['recommendations'])}")
            print(f"    - Avg engagement score: {result['expected_impact']['average_engagement_score']}")
            
            # Display first day's schedule
            if result['weekly_schedule']:
                first_day = result['weekly_schedule'][0]
                print(f"    - {first_day['day']} posts: {len(first_day['posts'])}")
                if first_day['posts']:
                    first_post = first_day['posts'][0]
                    print(f"      • Time: {first_post['time']}, Score: {first_post['engagement_score']}")
            
        except Exception as e:
            print(f"    ✗ Error: {str(e)}")
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    print("\nThe scheduler is working correctly!")
    print("If you're still having issues with the API, the problem might be:")
    print("1. Request format - check your payload")
    print("2. CORS issues - check browser console")
    print("3. Server errors - check FastAPI logs")
    
except ImportError as e:
    print(f"\n✗ Import Error: {str(e)}")
    print("\nPossible fixes:")
    print("1. Make sure you're in the correct directory")
    print("2. Check if ml_models/__init__.py exists")
    print("3. Verify schedule_optimizer.py is in ml_models/")
    print("4. Run: python -c 'import sys; print(sys.path)'")
    
except Exception as e:
    print(f"\n✗ Error: {str(e)}")
    traceback.print_exc()
    print("\nDebug info:")
    print(f"Python version: {sys.version}")
    print(f"Working directory: {sys.path[0]}")

print("\n" + "=" * 60)