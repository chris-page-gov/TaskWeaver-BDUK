from concurrent.futures import Executor

env_id = "your_env_id"  # Replace "your_env_id" with the actual value

executor = Executor(env_id, session_id, session_dir)
success, test_results = executor.test_plugin("paper_summary")