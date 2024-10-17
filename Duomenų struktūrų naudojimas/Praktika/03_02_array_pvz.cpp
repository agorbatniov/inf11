float kainos[5] = {10.5, 20.0, 5.99, 15.0, 8.75};
float brangiausia = kainos[0];
for (int i = 1; i < 5; i++) {
    if (kainos[i] > brangiausia) {
        brangiausia = kainos[i];
    }
}
cout << "Brangiausia prekė kainuoja: " << brangiausia << endl;  // Rezultatas: 20.0
