# Los cinco defectos descritos sin ejecutar nada

Muestra pequeña para hacer el laboratorio sin Python, copiando los casos en un chat. Las respuestas correctas están al final, plegadas: no abrirlas hasta haber anotado las propias.

Los cinco síntomas del módulo `gestor_licencias.py` descritos en lenguaje llano. Pegar el código y cada síntoma en el chat y pedir causa y corrección:

1. Una licencia que caduca hoy figura como caducada el mismo día (debería seguir válida hasta el final del día).
2. Se pueden asignar más usuarios que plazas contratadas.
3. Consultar el cliente que no tiene licencia hace que el programa se interrumpa con un error en lugar de devolver «ninguna».
4. Al buscar usuarios con un nombre de cliente especialmente construido se obtienen usuarios de otros clientes.
5. El registro de actividad guarda la contraseña de administrador y la que se esperaba en texto claro.

<details>
<summary>Respuestas correctas de la muestra</summary>

| Síntoma | Causa | Corrección |
|---|---|---|
| 1 | Se exige «más de 0 días restantes» en lugar de «0 o más» | Cambiar `> 0` por `>= 0` |
| 2 | Solo se rechaza si las plazas libres son negativas | Rechazar también cuando son 0 (`<= 0`) |
| 3 | Se accede al primer resultado de una lista vacía | Comprobar si hay resultado y devolver `None` |
| 4 | El nombre del cliente se concatena en la consulta (inyección SQL) | Usar una consulta con parámetros |
| 5 | Se escribe el token en el registro y se compara con `==` | No registrarlo y comparar con `hmac.compare_digest` |

</details>
