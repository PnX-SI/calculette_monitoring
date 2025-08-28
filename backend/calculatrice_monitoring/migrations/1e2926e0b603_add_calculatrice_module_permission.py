"""Add calculatrice module permission

Revision ID: 1e2926e0b603
Revises: 78ba67f597ee
Create Date: 2025-08-28 18:55:23.047899

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '1e2926e0b603'
down_revision = '78ba67f597ee'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO
            gn_permissions.t_permissions_available (
                id_module,
                id_object,
                id_action,
                label,
                scope_filter
            )
        SELECT
            m.id_module,
            o.id_object,
            a.id_action,
            v.label,
            v.scope_filter
        FROM
            (
                VALUES
                    ('CALCULATRICE', 'ALL', 'R', False, 'Accéder au module')
            ) AS v (module_code, object_code, action_code, scope_filter, label)
        JOIN
            gn_commons.t_modules m ON m.module_code = v.module_code
        JOIN
            gn_permissions.t_objects o ON o.code_object = v.object_code
        JOIN
            gn_permissions.bib_actions a ON a.code_action = v.action_code
        """
    )


def downgrade():
    # TODO
    pass
