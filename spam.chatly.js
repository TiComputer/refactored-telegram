function makeid(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLM!@#$%^&*() NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}

for (let i = 0; i < 100; i++) {
  socket.emit('message', {user: makeid(10), message: "Your message here"})
} 
