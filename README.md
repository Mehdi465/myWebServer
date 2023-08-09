# web_server_for_learning_words



 <th scope="col">ID</th>
                <th scope="col">Word</th>
                <th scope="col">Your answer</th>
                <th scope="col"></th>
                <th scope="col"></th>
            </tr>
        </thead>
        <tbody>
            <!-- Your rows inside the table HERE: -->
            {% for item in items %}
                <tr>
                    <td>{{ item.id }}</td>
                    <td>{{ item.word }}</td>
                    <td>{{ item.definition }}</td>
                    
                    <td>
                        <button class="btn btn-outline btn-info">show me the definition</button>
                        
                    </td>
                </tr>
            {% endfor %}