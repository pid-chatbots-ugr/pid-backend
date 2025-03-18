"""
Author: Angel Ruiz Zafra
License: MIT License
Version: 2025.2.1
Repository:  https://github.com/pid-chatbots-ugr/pid-backend
Created on 17/3/25 by Angel Ruiz Zafra
"""
import os
import time

from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from datetime import datetime

# Cargar las variables desde credentials.env
dotenv_path = find_dotenv("../credentials.env")  # Buscar en el nivel superior
load_dotenv(dotenv_path)

class MongoDBManager:
    def __init__(self):
        """
        Inicializa la conexión con MongoDB usando credenciales desde .env.
        """
        self.mongo_uri = os.getenv("MONGO_URI")
        self.db_name = os.getenv("MONGO_DB_NAME")
        self.collection_name = os.getenv("MONGO_COLLECTION")

        if not self.mongo_uri or not self.db_name or not self.collection_name:
            raise ValueError("Faltan variables de entorno para la conexión a MongoDB")

        # Conectar a la base de datos
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def insertar_conversacion(self, usuario, conversacion,metadata=None,timestamp = time.time()):
        """
        Inserta una nueva conversación en la colección.
        :param usuario: Nombre o ID del usuario.
        :param conversacion: Texto de la conversación.
        :return: ID del documento insertado.
        """
        documento = {
            "usuario": usuario,
            "conversación": conversacion,
            "timestamp": timestamp,
            "metadata": metadata
        }
        resultado = self.collection.insert_one(documento)
        return resultado.inserted_id

    def obtener_conversaciones(self, usuario=None):
        """
        Recupera todas las conversaciones o las de un usuario en específico.
        :param usuario: (Opcional) Filtra por usuario.
        :return: Lista de documentos encontrados.
        """
        filtro = {"usuario": usuario} if usuario else {}
        return list(self.collection.find(filtro, {"_id": 0}))  # Excluir _id si no lo necesitas

    def eliminar_conversacion(self, usuario):
        """
        Elimina todas las conversaciones de un usuario.
        :param usuario: Usuario del cual eliminar las conversaciones.
        :return: Número de documentos eliminados.
        """
        resultado = self.collection.delete_many({"usuario": usuario})
        return resultado.deleted_count

    def cerrar_conexion(self):
        """ Cierra la conexión con MongoDB. """
        self.client.close()

# Prueba si el archivo se ejecuta directamente
if __name__ == "__main__":
    db_manager = MongoDBManager()

    # Insertar datos de prueba
    id_insertado = db_manager.insertar_conversacion("usuario1", "Hola, esto es un mensaje de prueba.")
    print(f"Conversación insertada con ID: {id_insertado}")

    # Obtener todas las conversaciones
    conversaciones = db_manager.obtener_conversaciones()
    print("Conversaciones en la base de datos:", conversaciones)

    # Eliminar conversaciones de un usuario
    #eliminados = db_manager.eliminar_conversacion("usuario1")
    #print(f"Conversaciones eliminadas: {eliminados}")

    # Cerrar la conexión
    db_manager.cerrar_conexion()
