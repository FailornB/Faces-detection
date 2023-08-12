import cv2

# Charge le classificateur de visage pré-entraîné
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fonction pour détecter et dessiner des rectangles autour des visages
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        center = (x + w // 2, y + h // 2)
        cv2.circle(image, center, 5, (0, 255, 0), -1)
    return image



# Demande à l'utilisateur d'entrer le chemin de la photo ou de la vidéo
input_path = input("Entrez le chemin de la photo ou de la vidéo : ")

# Vérifie si le chemin correspond à une image ou une vidéo
if input_path.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
    image = cv2.imread(input_path)
    result_image = detect_faces(image)
    cv2.imshow('Face Detection', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif input_path.endswith(('.mp4', '.avi', '.mov')):
    cap = cv2.VideoCapture(input_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        result_frame = detect_faces(frame)
        cv2.imshow('Face Detection Video', result_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Format de fichier non pris en charge.")




def main():
    detect_faces(image);