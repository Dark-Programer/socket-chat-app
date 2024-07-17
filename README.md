<h1>Chat Application</h1>
    <p>This is a simple chat application built using Python's socket and threading libraries. The application consists of a server and multiple clients, enabling multiple users to communicate with each other in real-time.</p>
    
<h2>Features</h2>
    <ul>
        <li>Real-time communication between multiple clients</li>
        <li>Nickname identification for each client</li>
        <li>Broadcasts messages to all connected clients</li>
        <li>Handles client disconnections gracefully</li>
    </ul>
    
<h2>Prerequisites</h2>
    <p>Python 3.x</p>
    
<h2>Installation</h2>
    <p>Clone the repository:</p>
    <pre><code>
    git clone https://github.com/yourusername/chat-application.git
    cd chat-application
    </code></pre>
    
<p>Create a virtual environment and activate it (optional but recommended):</p>
    <pre><code>
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    </code></pre>
    
<p>Install any required packages (none required for this simple implementation, but can be added as needed):</p>
    <pre><code>
    pip install -r requirements.txt  # If you add any dependencies in the future
    </code></pre>
    
<h2>Usage</h2>
    <h3>Server</h3>
    <p>Run the server:</p>
    <pre><code>
    python server.py
    </code></pre>
    <p>The server will start listening for client connections.</p>
    
<h3>Client</h3>
    <p>Run the client:</p>
    <pre><code>
    python client.py
    </code></pre>
    <p>Enter your nickname when prompted.</p>
    <p>Start chatting!</p>
    
<h2>Files</h2>
    <ul>
        <li><strong>server.py</strong>: Contains the server code.</li>
        <li><strong>client.py</strong>: Contains the client code.</li>
    </ul>
    
<h2>How It Works</h2>
    <h3>Server</h3>
    <ul>
        <li>The server listens for incoming client connections.</li>
        <li>When a client connects, the server requests the client's nickname.</li>
        <li>The server broadcasts messages to all connected clients.</li>
        <li>If a client disconnects, the server removes the client from the list and notifies the remaining clients.</li>
    </ul>
    
<h3>Client</h3>
    <ul>
        <li>The client connects to the server.</li>
        <li>The client sends its nickname to the server.</li>
        <li>The client listens for messages from the server and displays them.</li>
        <li>The client sends user-inputted messages to the server for broadcasting.</li>
    </ul>
    
<h2>Contributing</h2>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (git checkout -b feature-branch).</li>
        <li>Make your changes.</li>
        <li>Commit your changes (git commit -m 'Add some feature').</li>
        <li>Push to the branch (git push origin feature-branch).</li>
        <li>Open a pull request.</li>
    </ol>
    
<h2>Author</h2>
    <p>Arka Chakraborty</p>

<h2>Screenshots</h2>
    <<img src="">