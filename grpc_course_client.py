import grpc

import course_service_pb2
import course_service_pb2_grpc


def run():
    # Подключаемся к нашему серверу
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_service_pb2_grpc.CourseServiceStub(channel)

    # Передаем в запрос ID "api-course" согласно заданию
    request = course_service_pb2.GetCourseRequest(course_id="api-course")
    response = stub.GetCourse(request)

    # Печатаем ответ в консоль
    print(response)


if __name__ == "__main__":
    run()
