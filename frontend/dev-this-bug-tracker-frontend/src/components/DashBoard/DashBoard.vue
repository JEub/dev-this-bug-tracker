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
const isModalVisible= ref(false)
// ##### added ######
const toggleModal = () => {
    alert( 'You toggled open modal' );
    isOpen.value = !isOpen.value;
    return toggleModal;
};
const createToggle = () => {
    alert( 'You toggled create modal' );
    // createOpen.value = !createOpen.value;
    isModalVisible.value = !isModalVisible.value;
    return createToggle;
};
// ######
</script>


<script>
    const searchTerm = ref('');

    export default {
        name: 'DashBoard',
        components: {
            CreateEditTicket,
            TicketModal
        },
        data () {
            return {
                tableData: tickets,
                rowsPerPage: 5,
                currentPage: 1,
                modalData: null,
                isModalVisible: false,
            };
        },
        computed: {
            totalRows() {
                return this.tableData.length;
            },
            totalPages() {
                return Math.ceil(this.totalRows / this.rowsPerPage);
            },
            currentPageData() {
                const startIndex = (this.currentPage - 1) * this.rowsPerPage;
                const endIndex = startIndex + this.rowsPerPage;
                return this.tableData.slice(startIndex, endIndex);
            },
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
            },
            prevPage() {
                if(this.currentPage > 1) {
                    this.currentPage--;
                }
            },
            nextPage() {
                if (this.currentPage < this.totalPages) {
                    this.currentPage++;
                }
            },
            gotoPage(pageNumber) {
                this.currentPage = pageNumber;
            },
            close() {
            // uses Options API to emit a custom event
                this.$emit('close');
            },
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

        <table id="myTable" class="dashboard-table">
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
                <tr v-for="(row, index) in currentPageData" :key="index" class="ticket-data" @click="showModal(ticket)">
                    <DashBoard_Table_Row 
                    v-if="row.id.includes(searchTerm) || ticket.title.includes(searchTerm) || ticket.assigned_user.username.includes(searchTerm) || ticket.created_date.includes(searchTerm)" :ticketData="row" 
                    />
                </tr>
            </tbody>
            
        </table>
        <nav>
            <div class="pagination">
                <button @click="prevPage" :class="{ disabled: currentPage === 1 }">Previous</button>
                <button v-for="pageNumber in totalPages"
                    :key="pageNumber"
                    @click="gotoPage(pageNumber)"
                    :class="{ active: currentPage === pageNumber }"
                >
                {{ pageNumber }}
                </button>
                <button @click="nextPage" :class="{ disabled: currentPage === totalPages }">Next</button>
            </div>
        </nav>
    </div>
        <!-- <CreateEditTicket
        v-show="isModalVisible"
        @close="closeModal"
        class="modal-popup"
        :ticket="modalData"
        /> -->
    <CreateEditTicket
        v-show="isModalVisible"
        @click="toggleModal"
    />
    <!--### ADDED ###-->
    <div class="root" >
        <button @click="createToggle">Create Ticket</button>
        <teleport to="body">
            <div class="modal" v-if="isModalVisible">
                <!-- note: change onclikc to on close so form input can be clocked without closing modal-->
                <CreateEditTicket
                    @close="createToggle"
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
    /* @import 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css';
    @import 'https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css'; */
</style>