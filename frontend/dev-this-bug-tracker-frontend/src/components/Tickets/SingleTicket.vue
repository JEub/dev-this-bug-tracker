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
            ticketData: Object
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
    onMounted(() => console.log(ticketData.value));
</script>
<template>
    <!--<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true" >-->
            <div id="modal-dialog" v-if="isModalVisible=true">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3 id="singleTicketLabel">Ticket id </h3>
                        <h3>Creator contact email</h3>
                        <h3>Assigned users</h3>
                        <h3>Ticket status</h3>
                        <!--<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>-->
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <p>Date opened / closed</p>
                        </div>
                        <div class="header">
                            <p>Title</p>
                            <p>Description</p>
                        </div>
                        <div class="row">Groups</div>
                        <div class="row">Story points</div>
                        <div class="row">
                            <ul>
                                <li>Parent ticket links</li>
                            </ul>
                        </div>
                        <div class="row">
                            <ul>
                                <li>History of assigned users w/time worked on ticket</li>
                            </ul>
                        </div>
                        <div class="row">
                            <p>Ticket tags</p>
                        </div>
                        <div class="row bigRow">
                            <button class="btn btn-primary sm">Add Comment</button>
                            <div class="hide">
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
                    <div class="modal-footer">
                        <!--Set up this edit ticket to open edit modal-->
                        <button class="btn btn-success">Edit Ticket</button>
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