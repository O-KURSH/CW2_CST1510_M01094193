from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.data.incidents import (
    load_csv_to_table,
    insert_incident,
    get_all_incidents,
    update_incident_status,
    delete_incident
)
from app.services.user_service import register_user, login_user


def main():
    conn = connect_database()

    # 1. Create tables
    create_all_tables(conn)

    # 2. Load CSV files
    load_csv_to_table(conn, "DATA/cyber_incidents.csv", "cyber_incidents")
    load_csv_to_table(conn, "DATA/datasets_metadata.csv", "datasets_metadata")
    load_csv_to_table(conn, "DATA/it_tickets.csv", "it_tickets")

    # 3. Test user registration & login
    success, msg = register_user("alice2", "SecurePass123!", "analyst")
    print(msg)

    success, msg = login_user("alice2", "SecurePass123!")
    print(msg)

    # 4. Test CRUD on incidents
    print("\n=== TESTING INCIDENT CRUD ===")

    # Create
    new_id = insert_incident(
        conn,
        "2024-02-01",
        "Phishing",
        "High",
        "Open",
        "User received a phishing email",
        "alice2"
    )
    print(f"Inserted incident ID: {new_id}")

    # Read
    df = get_all_incidents(conn)
    print("\nCurrent Incidents:")
    print(df.head())

    # Update
    updated = update_incident_status(conn, new_id, "Resolved")
    print(f"\nUpdated Rows: {updated}")

    # Delete
    deleted = delete_incident(conn, new_id)
    print(f"Deleted Rows: {deleted}")

    conn.close()
    print("\nProgram finished.")


if __name__ == "__main__":
    main()


