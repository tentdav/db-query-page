select p.firstname, p.lastname, d.name from person p join employeedepartmenthistory edh on p.businessentityid = edh.businessentityid join department d on edh.departmentid  = d.departmentid ;



select groupname, count(*) as cantidad_departamentos from department group by groupname;



select s.name, count(*) cantidad_empleados from shift s join employeedepartmenthistory edh on s.shiftid = edh.shiftid group by s.name;