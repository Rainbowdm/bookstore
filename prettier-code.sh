#!/bin/bash

black app/main.py

black app/utils/constants.py
black app/utils/pure_db.py
black app/utils/orm_db.py
black app/utils/db_functions.py
black app/utils/helper_functions.py
black app/utils/redis_object.py
black app/utils/security.py
black app/utils/db_objects.py

black app/tests/all_tests.py
black app/tests/locust_load_test.py

black app/routes/v1.py
black app/routes/v2.py

black app/models/author.py
black app/models/book.py
black app/models/jwt_user.py
black app/models/user.py
