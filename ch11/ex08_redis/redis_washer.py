# p354

import redis

conn = redis.Redis()
print("Washer is starting")
dishes = ["salad", "bread", "entree", "dessert"]
for dish in dishes:
    msg = dish.encode("utf-8")
    conn.rpush("dishes", msg)
    print("Washed", dish)
conn.rpush("dishes", "quit")
print("Washer is done")
