// script.js
const userAvatar = new Image();
userAvatar.src = "bot.png";


// 显示conversation框
document.getElementById('conversation').style.display = 'block';
appendMessage('bot', '你好，这里是"虚空 文献阅读助手！"');

function loadPDF() {
    const pdfInput = document.getElementById('pdf-input');
    const pdfIframe = document.getElementById('pdf-iframe');
    // 获取选择的文件
    const selectedFile = pdfInput.files[0];
    if (selectedFile) {
    // 创建一个Blob URL以显示所选的PDF文件
        const objectURL = URL.createObjectURL(selectedFile);
        pdfIframe.src = objectURL;
    }
}

function appendMessage(who, text) {
    const conversation = document.getElementById('conversation');
    const message = document.createElement('div');
    message.className = 'message ' + who;
    console.log("111111")
    // 创建气泡元素
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text;
    bubble.style.whiteSpace = 'pre-line'; // 允许换行

    // 创建头像元素
    const avatar = document.createElement('div');
    avatar.className = 'avatar';

    // 如果是用户，先添加气泡，再添加头像
    if (who === 'user') {
        message.appendChild(bubble);
        message.appendChild(avatar);
    } else {
        // 如果是机器人，先添加头像，再添加气泡
        message.appendChild(avatar);
        message.appendChild(bubble);
    }

    conversation.appendChild(message);
    conversation.scrollTop = conversation.scrollHeight;
}

function submitQuestion() {
    const query = document.getElementById('user-input').value;
    appendMessage('user', query);
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:8000/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) 
    {
        if (xhr.status === 200) 
        {
            const result = JSON.parse(xhr.responseText);
            // 使用机器人回答调用appendMessage函数
            appendMessage('bot', result.answer);
            console.log(result)
        }
    }
    };
    const data = JSON.stringify({query});
    // 清空输入框
    document.getElementById('user-input').value = '';
    xhr.send(data);
}
