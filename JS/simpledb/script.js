const addSubtaskBtn = document.getElementById('addSubtaskBtn');
        const subtasksContainer = document.getElementById('subtasksContainer');

        // Initialize IndexedDB
        let db;
        const request = indexedDB.open('TaskDB', 1);

        request.onupgradeneeded = function(event) {
            db = event.target.result;
            db.createObjectStore('tasks', { keyPath: 'id', autoIncrement: true });
        };

        request.onsuccess = function(event) {
            db = event.target.result;
        };

        // Function to add a new subtask input
        addSubtaskBtn.addEventListener('click', () => {
            const subtaskDiv = document.createElement('div');
            subtaskDiv.className = 'subtask';
            subtaskDiv.innerHTML = `
                <input type="text" name="subtask[]" placeholder="Subtask" required>
                <button type="button" class="remove-btn" onclick="removeSubtask(this)">Remove</button>
            `;
            subtasksContainer.appendChild(subtaskDiv);
        });

        // Function to remove a subtask input
        function removeSubtask(button) {
            const subtaskDiv = button.parentElement;
            subtasksContainer.removeChild(subtaskDiv);
        }

        // Form submission
        document.getElementById('taskForm').addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission behavior
            const formData = new FormData(event.target); // Collect form data

            // Get main task value
            const mainTask = formData.get('mainTask');
            console.log("Main Task:", mainTask);

            // Get subtasks values
            const subtasks = formData.getAll('subtask[]');
            console.log("Subtasks:", subtasks);

            // Save to IndexedDB
            const taskData = { mainTask, subtasks };
            saveTask(taskData);
        });

        // Function to save task to IndexedDB
        function saveTask(task) {
            const transaction = db.transaction(['tasks'], 'readwrite');
            const store = transaction.objectStore('tasks');
            store.add(task);

            transaction.onsuccess = function() {
                console.log('Task saved:', task);
            };

            transaction.onerror = function(event) {
                console.error('Error saving task:', event.target.error);
            };
        } 