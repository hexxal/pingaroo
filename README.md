# pingaroo

Here be dragons.

# Setup

1. Create and activate venv

    `python -m venv venv && source venv/bin/activate`

2. Copy `local_settings.py` from template

    `cp local_settings.py.tpl local_settings.py`

3. Build the containers

    `docker compose up -d`

3. Start up celery and celery beat scheduler

    ```
    python -m celery -A project worker -l INFO
    python -m celery -A project beat
    ```
