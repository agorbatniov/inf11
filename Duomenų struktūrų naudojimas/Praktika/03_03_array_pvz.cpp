int temp[7] = {20, 22, 19, 21, 23, 20, 18};
int temp_min = temp[0], temp_max = temp[0];
for (int i = 1; i < 7; i++) {
    if (temp[i] < temp_min) temp_min = temp[i];
    if (temp[i] > temp_max) temp_max = temp[i];
}
cout << "Mažiausia temperatūra: " << temp_min << endl;  // Rezultatas: 18
cout << "Didžiausia temperatūra: " << temp_max << endl;  // Rezultatas: 23
