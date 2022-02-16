import json


def get_all_candidates(cursor):
    cursor.execute("SELECT * FROM candidates")

    # this will extract row headers
    row_headers = [x[0] for x in cursor.description]

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()

    return json.dumps({'number_of_candidates': len(json_data), 'candidates': json_data})
