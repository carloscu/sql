USE etl_db;

select tbl_traffic_2.index, tbl_traffic_2.Year, tbl_traffic_2.Gender, parking_db.Color, tbl_make.MAKE_DESC
from  tbl_traffic_2, parking_db, tbl_make where tbl_traffic_2.Make=tbl_make.﻿MAKE and parking_db.Make=tbl_make.﻿MAKE;


