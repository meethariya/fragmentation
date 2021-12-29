from frag.store import connector

def insert(value):
    conn,cur = connector()
    cur.execute("USE ads1_1;")
    name = "pr"
    price = 0
    seller = "sel"
    category = "cat"
    for i in range(value):
        cur.execute(f"INSERT INTO product(name,price,seller,category) VALUES('{name+str(i)}',{price+i},'{seller+str(i)}','{category+str(i)}');")
    conn.commit()

insert(10000)