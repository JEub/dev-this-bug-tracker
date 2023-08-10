<script setup>
    import { ref, onMounted} from 'vue';
    // refactor into one piece with key value relationships
    // const title = ref(this.ticketData.title)
    // const description = ref(this.ticketData.description)
    // const storyPoints = ref(this.ticketData.storyPoints)
    const ticketStatus = ref([ 
        {id:0, name:'Open'},
        {id:1, name:'In Progess'},
        {id:2, name:'Blocked'},
        {id:3, name:'Needs More Info'},
        {id:4, name:'Closed'},
        {id:5, name:'Cancelled'}
    ])
    // // const groups = ref([this.ticketData.groups])
    // const assignedUser = ref([this.ticketData.asignedUser])
    // const parentLinks = ref(this.ticketData.parentLinks)
    // const ticketTags = ref(this.ticketData.ticketTags)
    // const ticketComments = ref(this.ticketData.ticketComments)
    

    // {id:0, name:'Open'},
    //     {id:1, name:'In Progess'},
    //     {id:2, name:'Blocked'},
    //     {id:3, name:'Needs More Info'},
    //     {id:4, name:'Closed'},
    //     {id:5, name:'Cancelled'}
    // const isOpen = ref(false)
    // const createOpen = ref(false)
    // const isModalVisible = ref(false)
    // onMounted(() => console.log(ticketproperty.value))

    
</script>
<script>
    // const title = ref(null);
    // const description = ref(this.ticketData.description);
    // const storyPoints = ref(this.ticketData.storyPoints);
    // const ticketStatus = ref([this.ticketData.ticketStatus]);
    // const groups = ref([this.ticketData.groups]);
    // const assignedUser = ref([this.ticketData.asignedUser]);
    // const parentLinks = ref(this.ticketData.parentLinks);
    // const ticketTags = ref(this.ticketData.ticketTags);
    // const ticketComments = ref(this.ticketData.ticketComments);
    export default {
        name: 'CreateEditTicket',
        props: {    
            ticketData: {
                "id": String,
                "title": String,
                "description": String,
                "start_date": Date,
                "completed_date": Date,
                "status_id": Number,
                "creator": {
                    "id": String,
                    "username": String,
                    "email": String
                },
                "assigned_user": {
                    "id": Number,
                    "username": String,
                    "email": String
                }, 
                "created_date": Date,
                "last_update": Date,
            },
            newData: {
                "title": String,
                "description": String,
                "storyPoints": String,
                "ticketStatus": String
            },
        },
        methods: {
            // close () {
            //     emit('close');
            // },
            close() {
            // uses Options API to emit a custom event
                this.$emit('close');
            },
            // onSubmit(event) {
            //     event.preventDefault()
            //     alert(JSON.stringify(this.form))
            // },
            // onReset(event) {
            //     event.preventDefault()
            //     // Reset our form values
            //     this.form.email = ''
            //     this.form.name = ''
            //     this.form.food = null
            //     this.form.checked = []
            //     // Trick to reset/clear native browser form validation state
            //     this.show = false
            //     this.$nextTick(() => {
            //     this.show = true
            //     })
            // },
        },
    };

</script>

<template>
    <!-- v-if="isModalVisible=true" -->
    <div class="modal">
        <!-- entire form will require prepopulate of data from database upon edit function -->  
        <div id="wrapper">
        <form action="" class="body">
            <div>
                <!--minimum required -->
                <!--fix ref or vmodel to stop saving this on close-->
                <div class="row">
                    <label for="title">Title: </label>
                    <!-- enter values for editing form -->
                    <!-- ="title" -->
                    <input id="title" v-model="ticketData.title" /> 
                </div>
                <div class="row">
                    <label for="description">Description: </label>
                    <!-- enter values for editing form -->
                    <input v-model = "ticketData.description" id="description"/> 
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
                    <select v-model=" ticketData.status_id" >
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
                <!-- ####### ADD CALLBACK TO DATABASE HERE WITH V-FOR TO ITERATE THROUGH USERS IN DATABASE #########-->
                <div class="row">
                    <label>Assign A User: </label>
                    <!-- call users from database here. map through values conditionally render each name with new input using map and filter -->
                    <!--<select v-model="assignedUser">
                        <option>Jack</option>
                        <option>Jill</option>
                        <option>Jenkins</option>
                    </select>
                    <span>Assigned Users: {{ assignedUser }}</span> -->
                    <input type="checkbox" id="jack" value="Jack" v-model="ticketData.assigned_user.username">
                    <label for="jack">Jack </label>
                    
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
                    <button type="submit" class=" button">Submit / Update</button>
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