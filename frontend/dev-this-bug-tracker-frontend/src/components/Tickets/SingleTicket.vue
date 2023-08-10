<script setup>
    import { ref, onMounted } from 'vue';
    import tickets from '../DashBoard/tickets.json';

    const title = ref('Title')
    const description = ref('Description')
    const storyPoints = ref('Story Points')
    const ticketStatus = ref('Open')
    const groups = ref(['Retail'])
    const assignedUser = ref(['Jack'])
    const parentLinks = ref('Parent Links')
    const ticketTags = ref('Ticket Tags')
    const ticketComments = ref('Ticket Comments')
    // add user to ticket
    // add comment button for view
</script>
<!-- Add change here to incluide ticket data on single ticket view -->
<script>
    export default {
        name: 'SingleTicket',
        props: {
            "ticketData": Object,
            openEditTicket: {
                type: Function
            },
        },

        // emit: ['close'],
        methods: {
            // close () {
            //     emit('close');
            // },
            close() {
            // uses Options API to emit a custom event
                this.$emit('close');
            },
        },
        
    };
    // onMounted(() => console.log(this.ticket));
</script>
<template>
            <div id="modal-dialog" v-if="isModalVisible=true">
                <div class="modal-content">
                    <div class="dismiss-row">
                        <div class="modal-row">
                            <h3 id="singleTicketLabel">Id: {{ ticketData.id }}</h3>
                            <h3>Created By: {{ ticketData.creator.email }}</h3>
                            <h3>Assigned User: {{ ticketData.assigned_user.username }}</h3>
                            <h3>Ticket Status: {{ ticketData.status_id }}</h3>
                        </div>
                        <div>
                            <button type="button" class="btn btn-danger" @click="close">X</button>
                        </div>
                    </div>
                    <div>
                        <p>_________________________________________________________________________________________</p>
                    </div>
                    <div class="modal-row">
                        <div class="row">
                            <!-- This was created / completed but we have 3 dates established in a ticket -->
                            <p><em>Start Date:</em> {{ ticketData.start_date }}<p>
                            </p><em>Completed Date:</em> {{ ticketData.completed_date }}</p> 
                        </div>
                        <div class="row">
                            <p><em>Title:</em> {{ ticketData.title }}</p>
                        </div>
                        <div class="row">
                            <p class="scroll"><em>Description:</em> {{ ticketData.description }}</p>
                        </div>
                        <div class="row">
                            <p><em>Groups</em></p>
                        </div>
                        <div class="row">
                            <p><em>Story points</em></p>
                        </div>
                        <div class="row">
                            <ul><em>Parent ticket links</em>
                                <li>Links</li>
                            </ul>
                        </div>
                        <div class="row">
                            <ul><em>History of assigned users w/time worked on ticket</em>
                                <li>Users</li>
                            </ul>
                        </div>
                        <div class="row">
                            <p><em>Ticket tags</em></p>
                        </div>
                        <div id="big" class="row">
                            <button class="btn btn-primary">Add Comment</button>
                            <div class="scroll">
                                <p>Ticket comments 1</p>
                                <p>Ticket comments 2</p>
                                <p>Ticket comments 3</p>
                                <p>Ticket comments 4</p>
                                <p>Ticket comments 5</p>
                                <p>Ticket comments 6</p>
                                <p>Ticket comments 7</p>
                                <p>Ticket comments 8</p>
                                <p>Ticket comments 9</p>
                                <p>Ticket comments 10</p>
                            </div>
                        </div>
                    </div>
                    <div class="dismiss-row">
                        <!--Set up this edit ticket to open edit modal-->
                        <button class="btn btn-success" @click="openEditTicket('editTicket', ticketData)">Edit Ticket</button>
                        <!--bootstrap close
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>-->
                        <!--emit close button-->
                        <button type="button" class="btn btn-danger" @click="close">Close</button>
                    </div>
                    
                </div>
            </div>
    <!--</div>-->
</template>

<style>
@import './styles/SingleTicket.css';
</style>