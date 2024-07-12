from celery import shared_task


@shared_task
def test_task(a: int, b: int) -> int:
    print("test Celery task : ", a + b)
    return a + b
