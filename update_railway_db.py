import mysql.connector

try:
    conn = mysql.connector.connect(
        host="kodama.proxy.rlwy.net",
        user="root",
        password="wdEzDuwChqTFgziUaDkVJIfDePEajgjT",
        database="railway",
        port=45867
    )

    cursor = conn.cursor()

    # Add columns (without IF NOT EXISTS for compatibility with older MySQL versions)
    try:
        cursor.execute("ALTER TABLE properties ADD COLUMN image_data LONGBLOB NULL AFTER images")
    except mysql.connector.Error as e:
        if "Duplicate column name" in str(e):
            print("Column image_data already exists")
        else:
            raise
    
    try:
        cursor.execute("ALTER TABLE properties ADD COLUMN image_mimetype VARCHAR(50) NULL AFTER image_data")
    except mysql.connector.Error as e:
        if "Duplicate column name" in str(e):
            print("Column image_mimetype already exists")
        else:
            raise

    conn.commit()
    cursor.close()
    conn.close()

    print("✓ Columns added successfully!")
except Exception as e:
    print(f"Error: {e}")
