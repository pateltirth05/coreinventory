from models.operation import Operation


def get_operations(db, type=None, status=None, warehouse=None):

    query = db.query(Operation)

    if type:
        query = query.filter(Operation.type == type)

    if status:
        query = query.filter(Operation.status == status)

    if warehouse:
        query = query.filter(
            (Operation.source_warehouse == warehouse) |
            (Operation.destination_warehouse == warehouse)
        )

    operations = query.all()

    results = []

    for op in operations:
        results.append({
            "id": op.id,
            "type": op.type,
            "status": op.status,
            "source_warehouse": op.source_warehouse,
            "destination_warehouse": op.destination_warehouse
        })

    return results