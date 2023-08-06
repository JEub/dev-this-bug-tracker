<script setup>
import { ref } from 'vue';
import tickets from './tickets.json';
import CreateEditTicket from '../Tickets/CreateEditTicket.vue';
import TicketModal from '../Tickets/TicketModal.vue';
// import users from './users.json';
import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';

const searchTerm = ref('');
const isOpen = ref(false)
const createOpen = ref(false)
// ##### added ######
const toggleModal = () => {
    alert( 'You toggled open modal' );
    isOpen.value = !isOpen.value;
    return toggleModal;
};
const createToggle = () => {
    alert( 'You toggled create modal' );
    createOpen.value = !createOpen.value;
    return createToggle;
};
// ######
</script>

<script>
    export default {
        name: 'DashBoard',
        components: {
            CreateEditTicket,
            TicketModal
        },
        data () {
            return {
                modalData: null,
                isModalVisible: false,
            };
        },
        methods: {
            showModal(ticketData) {
                console.log('test?');
                alert( 'You opened the modal from dashboard' );
                this.modalData = ticketData;
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
                alert( 'You closed the modal' );
            }
        },
    };
</script>

<template>
    <div class="dashboard">
        <div class="dashboard-header">
            <div>
                <button>All</button>
                <button>Mine</button>
            </div>
            <div>
                <input type='text' placeholder="Search" v-model="searchTerm"/>
                <button>Filter</button>
            </div>
        </div>
        <table class="table table-dark table-striped table-hover dashboard-table">
            <thead>
                <tr>
                    <th>
                        <h2>Id</h2>
                    </th>
                    <th>
                        <h2>Title</h2>
                    </th>
                    <th>
                        <h2>Assigned User</h2>
                    </th>
                    <th>
                        <h2>Status</h2>
                    </th>
                    <th>
                        <h2>Creation Date</h2>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ticket in tickets" :key="ticket.id" class="ticket-data" @click="showModal(ticket)">
                    <DashBoard_Table_Row 
                    v-if="ticket.id.includes(searchTerm) || ticket.title.includes(searchTerm) || ticket.assigned_user.username.includes(searchTerm) || ticket.created_date.includes(searchTerm)" :ticketData="ticket" 
                    />
                </tr>
            </tbody>
            <!-- Create a mapping function to display tickets retrieved from the database -->
        </table>
    </div>
    <!--@click="isModalVisable=true"
        @close="closeModal"
        class="modal-popup"
        :ticket="modalData" -->
    <CreateEditTicket
        v-show="isModalVisible"
        @click="toggleModal"
    />
    <!--### ADDED ###-->
    <div class="root" >
        <button @click="createToggle">Create Ticket</button>
        <teleport to="body">
            <div class="modal" v-if="createOpen">
                <!-- note: change onclikc to on close so form input can be clocked without closing modal-->
                <CreateEditTicket
                    @click="createToggle"
                    title="Create / Edit Ticket"
                />
            </div>
        </teleport>
        <button @click="toggleModal">Open</button>
        <teleport to="body">
            <div class="modal" v-if="isOpen">
                <TicketModal
                    @click="toggleModal"
                    title="Does this work?"
                    msg="I hope so"
                />
            </div>
        </teleport>
    </div>
</template>

<style>
    @import './DashBoard.css';
</style>