from tasks import add

# Call the background task
result = add.apply_async((10, 20))

# Wait for the task to complete and get the result
print(f'Task result: {result.get()}')