# backend_segunda_prueba_getxerpa

## A continuación el listado de los endpoints a consultar utilizando algún cliente para pruebas (ejemplo postman)

### http://localhost:8000/api/1.0/categorias 
### Muestra el listado completo de las categorías registradas en la BD (GET) y permite crear nuevas categorías (POST)

### http://localhost:8000/api/1.0/categorias/<int:categoria_id>
### Permite editar (PUT) o eliminar (DELETE) una categoría al reemplazar el <int:categoria_id> por el respectivo id de la categoría

### http://localhost:8000/api/1.0/transacciones/
### Muestra el listado completo de las transacciones registradas en la BD (GET) y permite crear nuevas transacciones (POST)

### http://localhost:8000/api/1.0/transacciones/<int:categoria_id>
### Muestra el listado de las transacciones correspondientes a la categoría deseada, se debe reemplazar <int:categoria_id> por el id correspondiente a la categoría que se desea (GET)

### http://localhost:8000/api/1.0/transacciones/mes/<int:categoria_id>'
### Muestra el listado de las transacciones realizadas para cierta categoría y las agrupa por mes, se debe reemplazar <int:categoria_id> por el id correspondiente a la categoría que se desea (GET)

## Ejemplo de parámetros requeridos para crear categorías

{
  "nombre": "Comida",
  "limite": 1500.0
}

## Ejemplo de parámetros requeridos para crear transacciones

{
  "descripcion": "uber",
  "monto": 30.0,
  "fecha": "2023-08-19T23:05:40Z",
  "ignorar": false,
  "id_categoria": 1
}
