from ultralytics import YOLO

# Carrega os pesos pré-treinados 'yolo11s.pt' para transferência de aprendizagem
model = YOLO('yolo11s.pt')

# Treina o modelo usando seus dados; ajuste o path para seu arquivo YAML com estrutura dos dados
model.train(data='yolo_dataset.yaml', epochs=100, imgsz=320, batch = 9, device='mps')

