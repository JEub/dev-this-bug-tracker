<script setup>
    import { ref, onMounted} from 'vue';
    // refactor into one piece with key value relationships
    const title = ref('Title')
    const description = ref('Description')
    const storyPoints = ref('Story Points')
    const ticketStatus = ref([
        {id:0, name:'Open'},
        {id:1, name:'In Progess'},
        {id:2, name:'Blocked'},
        {id:3, name:'Needs More Info'},
        {id:4, name:'Closed'},
        {id:5, name:'Cancelled'}
    ])
    const groups = ref(['Retail'])
    const assignedUser = ref(['Jack'])
    const parentLinks = ref('Parent Links')
    const ticketTags = ref('Ticket Tags')
    const ticketComments = ref('Ticket Comments')
    
    const isOpen = ref(false)
    // onMounted(() => console.log(ticketproperty.value))
</script>
<script>
    export default {
        name: 'CreateEditTicket',
        props: {
            ticket: Object
        },
        emit: ['close'],
        methods: {
            close() {
            // uses Options API to emit a custom event
                this.$emit('close');
            },
        },
    };
</script>

<template>

    <div class="modal" v-if="createOpen=true">
        
        <!-- entire form will require prepopulate of data from database upon edit function -->  
        <div id="wrapper">
        <form action="" class="body">
            <div>
                <!--minimum required -->
                <div class="row">
                    <label for="title">Title: </label>
                    <!-- enter values for editing form -->
                    <input v-model="title" id="title"/> 
                </div>
                <div class="row">
                    <label for="description">Description: </label>
                    <!-- enter values for editing form -->
                    <input v-model = "description" id="description"/> 
                </div>
                <div class="row">
                    <label for="content">Content: </label>
                    <!-- enter values for editing form -->
                    <textarea v-model = "storyPoints" id="content">{{ storyPoints }}</textarea>
                </div>
            </div>
            <div >
                <div class="row">
                    <label>Ticket Status: </label>
                    <!-- stored ticket status from db? -->
                    <!-- change up order of v-model and v-for? v-for loops over data that v-model is holding then binding back to ref -->
                    <select v-model="ticketStatus" >
                        <option v-for="(ticketStatus, index) in ticketStatus"
                        :key="ticketStatus.id">{{ index +1 }} : {{ ticketStatus.name }}</option>
                        <!-- <option>Open</option> 
                        <option>In Progress</option>
                        <option>Blocked</option>
                        <option>Need More Info</option>
                        <option>Closed</option>
                        <option>Cancelled</option> -->
                    </select>
                </div>
                
                <div class="row">
                    <label>Groups: </label>
                    <input type="checkbox" id="retail" value="Retail" v-model="groups">
                    <label for="retail">Retail </label>
                    <input type="checkbox" id="office" value="Office" v-model="groups">
                    <label for="office">Office </label>
                    <input type="checkbox" id="field" value="Field" v-model="groups">
                    <label for="field">Field </label>
                    <p>Current Groups: <pre>{{ groups }}</pre></p>
                    
                </div>
                
                <div class="row">
                    <label>Assign A User: </label>
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
                <div class="row">
                    <label for="parentLinks">Parent Links: </label>
                    <!-- link parent tickets with relationship in database -->
                    <textarea v-model = "parentLinks" id="ticketTags">{{ parentLinks }}</textarea>
                </div>
                <div class="row">
                    <label for="ticketTags">Ticket Tags: </label>
                    <!-- call ticket labels from database -->
                    <textarea v-model = "ticketTags" id="parentLinks">{{ ticketTags }}</textarea>
                </div>
                <div class="row">
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
        <button type="button" class="close button" @click="close">Close</button>
        </div>
    </div>
</template>

<style>
@import './styles/SingleTicket.css';
</style>