# celery-redis-cluster-backend
Our customized celery redis cluster backend.

# Install
`pip install -e git+https://github.com/ArticulateAI/celery-redis-cluster-backend.git#egg=celery-redis-cluster-backend`

# To use the package
Set the backend when creating celery
```
Celery(name, 
       backend="celery_redis_cluster_backend.redis_cluster.RedisClusterBackend")
```

Set your redis cluster address as environment variable
```
REDIS_HOST=localhost
REDIS_PORT=7000
```