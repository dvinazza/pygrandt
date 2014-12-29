pygrandt
========

jugadores mas populares

select jugadores.nombre, equipos.nombre, avg(equipos_gdt.cantidad) as popu
from equipos_gdt
left join jugadores 
on jugadores.id = equipos_gdt.jugador_id
left join equipos 
on equipos.id = jugadores.equipo_id
group by jugador_id
order by popu desc
limit 10

equipos populares

from equipos_gdt
left join jugadores 
on jugadores.id = equipos_gdt.jugador_id
left join equipos 
on equipos.id = jugadores.equipo_id 
where equipos_gdt.cantidad > 200
group by equipos.nombre
order by popu desc
limit 5
