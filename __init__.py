# -*- coding: utf-8 -*-

from openerp.sql_db import Cursor
from openerp.tools.config import config

def custom_autocommit(self, on):
    iso_mode = int(config.get("isolation_mode"))
    isolation_level = iso_mode
    self._cnx.set_isolation_level(isolation_level)
    
Cursor.autocommit = custom_autocommit