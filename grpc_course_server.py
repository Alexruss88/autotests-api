from concurrent import futures
import grpc

import course_service_pb2
import course_service_pb2_grpc


# Класс обработчик запросов сервера
class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):

    def GetCourse(self, request, context):
        # Возвращаем строго заданные в ТЗ строки
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )


def serve():
    # Запускаем сервер на пуле из 10 потоков
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    # Слушаем порт 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер курсов запущен на порту 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
