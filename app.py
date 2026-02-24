from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

def load_model():
    MODEL_PATH = 'model/flood_model.pkl'
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    return None

model = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Ambil data dari form
        hujan = float(request.form.get('curah_hujan'))
        sungai = float(request.form.get('jarak_sungai'))
        elevasi = float(request.form.get('ketinggian'))
        drain = float(request.form.get('drainase'))
        padat = float(request.form.get('kepadatan'))
        
        # 2. Prediksi menggunakan model
        final_features = np.array([[hujan, sungai, elevasi, drain, padat]])
        prediction = int(model.predict(final_features)[0]) # Ambil angka hasil prediksi

        # 3. Logika Hasil & Tindakan (Hanya satu return jsonify di sini)
        if prediction == 0:
            return jsonify({
                'result': 'AMAN',
                'desc': 'Kondisi lingkungan terpantau stabil.',
                'action': [
                    'Tetap jaga kebersihan saluran air di sekitar rumah.',
                    'Pantau terus prakiraan cuaca secara berkala.',
                    'Lakukan penanaman biopori untuk tabungan air tanah.'
                ]
            })
        elif prediction == 1:
            return jsonify({
                'result': 'WASPADA',
                'desc': 'Terdeteksi potensi genangan air di wilayah ini.',
                'action': [
                    'Pindahkan barang elektronik ke tempat yang lebih tinggi.',
                    'Bersihkan got atau drainase yang tersumbat sampah.',
                    'Siapkan tas siaga bencana (dokumen penting & obat-obatan).'
                ]
            })
        else: # Untuk status 2 (Bahaya)
            return jsonify({
                'result': 'BAHAYA',
                'desc': 'Risiko banjir tinggi terdeteksi! Segera lakukan mitigasi.',
                'action': [
                    'Matikan aliran listrik dan gas di seluruh rumah.',
                    'Segera evakuasi mandiri ke titik aman atau posko terdekat.',
                    'Amankan aset berharga dan ikuti instruksi petugas setempat.'
                ]
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Pakai 0.0.0.0 agar bisa dibuka di HP dalam satu Wi-Fi
    app.run(debug=True, host='0.0.0.0', port=5000)