**Convert Odoo Domain to SQL**

----------------------------------------------------

Actually this module is based on Odoo **_search** method on **models.py** file
this module will return SQL when you pass domain instead pass it to **psycopg2** then execute it

to use this module first install then call get_query method with domain as argument, like this

```
domain = ['|',('name','ilike','agus'), '&', ('street','ilike', 'Street 2'), ('email', 'ilike', 'gmail')]
query = self.env['res.partner'].get_query(domain)

print(query)
```

then the result is like this

```
SELECT "res_partner".id FROM "res_partner" WHERE (("res_partner"."active" = 'True')  AND  (("res_partner"."name"::text ilike '%agus%')  OR  (("res_partner"."street"::text ilike '%Street 2%')  AND  ("res_partner"."email"::text ilike '%gmail%'))))
```

If pass apply_ir_rules argument with value True, like this

```
domain = ['|',('name','ilike','agus'), '&', ('street','ilike', 'Street 2'), ('email', 'ilike', 'gmail')]
query = self.env['res.partner'].get_query(domain, apply_ir_rules=True)
```

The result query will add some extra where clause based on ir_rule (Access Right) and user that currently login, like this

```
SELECT "res_partner".id FROM "res_partner" WHERE (("res_partner"."active" = 'True')  AND  (("res_partner"."name"::text ilike '%agus%')  OR  (("res_partner"."street"::text ilike '%Street 2%')  AND  ("res_partner"."email"::text ilike '%gmail%')))) AND (((("res_partner"."partner_share" IS NULL or "res_partner"."partner_share" = false )  OR  ("res_partner"."company_id" in ('1')))  OR  "res_partner"."company_id" IS NULL )  AND  ((("res_partner"."type" != 'private') OR "res_partner"."type" IS NULL)  OR  "res_partner"."type" IS NULL ))
```

Visit my website [to get Odoo tutorial tips and tricks](https://ngasturi.id)
