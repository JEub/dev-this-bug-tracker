<script setup>
    import { ref, onMounted} from 'vue';
    const ticketStatus = ref([ 
        {id:0, name:'Open'},
        {id:1, name:'In Progess'},
        {id:2, name:'Blocked'},
        {id:3, name:'Needs More Info'},
        {id:4, name:'Closed'},
        {id:5, name:'Cancelled'}
    ])
    const groups = ref(['Retail'])
    // onMounted(() => console.log(ticketproperty.value))
</script>
<script>
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
            // uses Options API to emit a custom event
            close() {
                this.$emit('close');
            },
            // onSubmit(event) {
            //     event.preventDefault()
            //     alert(JSON.stringify(this.form))
            //  save ticket data to ref or state here
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
    <div id="modal-dialog" > 
        <div class="modal-content">
            <form action="" class="modal-row">
                <div class="header-row">
                    <h2>Create / Edit Ticket</h2>
                    <button type="button" class="btn btn-danger" @click="close">X</button>
                </div>
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
                <div class="row">
                    <label>Ticket Status: </label>
                    <!-- stored ticket status from db? -->
                    <!-- change up order of v-model and v-for? v-for loops over data that v-model is holding then binding back to ref -->
                    <select v-model=" ticketData.status_id" >
                        <option v-for="(ticketStatus, index) in ticketStatus"
                        :key="ticketStatus.id">{{ index +1 }} : {{ ticketStatus.name }}</option>
                    </select>
                </div>
                <!-- ### ADD INDENTIFIER HERE FOR GROUPS FROM DATABASE ###-->
                <div id="box">
                    <div>
                        <label>Groups: </label>
                        <input type="checkbox" id="retail" value="Retail" v-model="groups">
                        <label for="retail">Retail </label>
                        <input type="checkbox" id="office" value="Office" v-model="groups">
                        <label for="office">Office </label>
                        <input type="checkbox" id="field" value="Field" v-model="groups">
                        <label for="field">Field </label>
                    </div>
                    <div>
                        <p class="">Current Groups: <pre>{{ groups }}</pre></p>
                    </div>
                </div>
                <!-- ####### ADD CALLBACK TO DATABASE HERE WITH V-FOR TO ITERATE THROUGH USERS IN DATABASE #########-->
                <div class="row">
                    <label>Assign A User: </label>
                    <select v-model="ticketData.assigned_user.username">
                        <option>Jack</option>
                        <option>Jill</option>
                        <option>Jenkins</option>
                    </select>
                    <p>Assigned Users: <pre>{{ ticketData.assigned_user.username }}</pre></p>
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
                    <textarea v-model = "ticketComments" id="ticketComments" cols="30" rows="10" class="scroll"></textarea>
                </div>
                <div class="dismiss-row">
                    <!-- conditionally render submit or update if "state" is either new or existing -->
                    <div v-if="createVisable=true">
                        <button type="submit" class="btn btn-success">Submit</button>
                    </div>
                    <div v-if="editVisable=true">
                        <button type="submit" class="btn btn-success">Update</button>
                    </div>
                    <button type="button" class="btn btn-danger" @click="close">Close</button>
                </div>
                
            </form>
        </div>
    </div>
</template>

<style>
@import './styles/SingleTicket.css';
</style>