import psycopg2

def main():
    # Starts a test Postgres server
    pg = testing.postgresql.PostgresSql()
    conn = psycopg2.connect(**pg.dsn())

if __name__ == '__main__':
    main()
