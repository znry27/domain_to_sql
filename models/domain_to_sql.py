# -*- coding: utf-8 -*-

from odoo.osv import expression
from odoo import models
from odoo.release import version_info


def get_query(self, args, apply_ir_rules=False):
    
    query = self._where_calc(args)

    if apply_ir_rules:
        self._apply_ir_rules(query, 'read')
    
    from_clause, where_clause, where_clause_params = query.get_sql()

    where_str = where_clause and (" WHERE %s" % where_clause) or ''
    
    query_str = 'SELECT "%s".id FROM ' % self._table + from_clause + where_str
    
    where_clause_params = map(lambda x: "'" + str(x) + "'" , where_clause_params)

    return query_str % tuple(where_clause_params)

models.BaseModel.get_query = get_query