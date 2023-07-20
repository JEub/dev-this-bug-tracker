<script setup>
    import { ref } from 'vue';
    
    const title = ref('Title')
    const description = ref('Description')
    const storyPoints = ref('Story Points')
    const ticketStatus = ref('Open')
    const groups = ref(['Retail'])
    const assignedUser = ref(['Jack'])
    const parentLinks = ref('Parent Links')
    const ticketTags = ref('Ticket Tags')
    const ticketComments = ref('Ticket Comments')
</script>

<template>
    <!-- entire form will require prepopulate of data from database upon edit function -->  
    <form action="">
        <div>
            <!--minimum required -->
            <div>
                <label for="">Title: </label>
                <!-- enter values for editing form -->
                <input v-model = "title"/> {{ Title }}
            </div>
            <div>
                <label for="">Description: </label>
                <!-- enter values for editing form -->
                <input v-model = "description"/> 
            </div>
            <div>
                <label for="">Content: </label>
                <!-- enter values for editing form -->
                <textarea v-model = "storyPoints">{{ storyPoints }}</textarea>
            </div>
        </div>
        <div>
            <div>
                <label for="">Ticket Status: </label>
                <!-- stored ticket status from db? -->
                <select v-model = "ticketStatus">
                    {{ ticketStatus }}
                    <option>Open</option>
                    <option>In Progress</option>
                    <option>Blocked</option>
                    <option>Need More Info</option>
                    <option>Closed</option>
                    <option>Cancelled</option>
                </select>
            </div>
            
            <div>
                <label for="">Groups: </label>
                <input type="checkbox" id="retail" value="Retail" v-model="groups">
                <label for="retail">Retail </label>
                <input type="checkbox" id="office" value="Office" v-model="groups">
                <label for="office">Office </label>
                <input type="checkbox" id="field" value="Field" v-model="groups">
                <label for="field">Field </label>
                <p>Current Groups: <pre>{{ groups }}</pre></p>
                
            </div>
            
            <div>
                <label for="">Assign A User: </label>
                <!-- call users from database here. map through values conditionally render each name with new input using map and filter -->
                <!--<select v-model="assignedUser">
                    <option>Jack</option>
                    <option>Jill</option>
                    <option>Jenkins</option>
                </select>
                <span>Assigned Users: {{ assignedUser }}</span> -->
                <input type="checkbox" id="jack" value="Jack" v-model="assignedUser">
                <label for="jack">Jack </label>
                <input type="checkbox" id="jill" value="Jill" v-model="assignedUser">
                <label for="jill">Jill </label>
                <input type="checkbox" id="jenkins" value="Jenkins" v-model="assignedUser">
                <label for="jenkins">Jenkins </label>
                <p>Assigned Users: <pre>{{ assignedUser }}</pre></p>
            </div>
            <div>
                <label for="">Parent Links: </label>
                <!-- link parent tickets with relationship in database -->
                <textarea v-model = "parentLinks">{{ parentLinks }}</textarea>
            </div>
            <div>
                <label for="">Ticket Tags: </label>
                <!-- call ticket labels from database -->
                <textarea v-model = "ticketTags">{{ ticketTags }}</textarea>
            </div>
            <div>
                <label for="ticketComments">Ticket Comments: </label>
                <!-- call ticket comments from database -->
                <textarea v-model = "ticketComments" id="ticketComments" cols="30" rows="10"></textarea>
            </div>
            <div>
                <!-- conditionally render submit or update if "state" is either new or existing -->
                <button type="submit">Submit / Update</button>
            </div>
        </div>
    </form>

</template>