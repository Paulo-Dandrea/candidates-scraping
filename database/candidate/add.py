def add_candidate(cnx, cursor, name: str, score: float, cpf: str):
    add_candidates = ("INSERT INTO candidates "
                      "(name, score, cpf) "
                      "VALUES (%s, %s, %s)")

    data_candidates = (name, score, cpf)

    cursor.execute(add_candidates, data_candidates)
    cnx.commit()

    return 'Ok - inserted'