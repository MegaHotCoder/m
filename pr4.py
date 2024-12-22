import cv2
from matplotlib import pyplot as plt

# 실제 이미지 경로
image_path = "C:/Users/piosp/OneDrive/english/english/image.jpg"

class EdgeDetector:
    def __init__(self):
        self.image = None
        self.gray_image = None
        self.edges = None

    def load_image(self, filepath):
        self.image = cv2.imread(filepath)
        if self.image is None:
            print("Error: 이미지를 로드할 수 없습니다. 파일 경로를 확인하세요.")
        else:
            print("이미지를 성공적으로 로드했습니다.")

    def convert_to_grayscale(self):
        if self.image is not None:
            self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
        else:
            print("Error: 먼저 이미지를 로드하세요.")

    def detect_edges(self, threshold1, threshold2):
        if self.gray_image is not None:
            self.edges = cv2.Canny(self.gray_image, threshold1, threshold2)  # Canny 엣지 검출
        else:
            print("Error: 먼저 그레이스케일 이미지를 변환하세요.")

    def show_images(self):
        if self.image is not None and self.gray_image is not None and self.edges is not None:
            # OpenCV는 BGR 형식이므로 RGB로 변환
            image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            plt.figure(figsize=(10, 4))

            # 원본 이미지 표시
            plt.subplot(1, 3, 1)
            plt.imshow(image_rgb)
            plt.title('Original Image')
            plt.axis('off')

            # 그레이스케일 이미지 표시
            plt.subplot(1, 3, 2)
            plt.imshow(self.gray_image, cmap='gray')
            plt.title('Grayscale Image')
            plt.axis('off')

            # 엣지 이미지 표시
            plt.subplot(1, 3, 3)
            plt.imshow(self.edges, cmap='gray')
            plt.title('Edge Detection') 
            plt.axis('off')

            plt.show()
        else:
            print("Error: 모든 이미지가 준비되지 않았습니다.")

# 객체 생성 및 이미지 처리
detector = EdgeDetector()
detector.load_image(image_path)  # 실제 경로를 전달
detector.convert_to_grayscale()
detector.detect_edges(100, 200)
detector.show_images()