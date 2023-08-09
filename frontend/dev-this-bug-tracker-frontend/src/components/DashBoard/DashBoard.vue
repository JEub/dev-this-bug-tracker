<script setup>
import { ref } from 'vue';
import tickets from './tickets.json';
import CreateEditTicket from '../Tickets/CreateEditTicket.vue';
import TicketModal from '../Tickets/TicketModal.vue';
import SingleTicket from '../Tickets/SingleTicket.vue';
// import users from './users.json';
import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';

// const searchTerm = ref('');
// const isOpen = ref(false)
// const singleTicketOpen = ref(false)
// const isModalVisible= ref(false)
// const toggleModal = () => {
//     alert( 'You toggled open modal' );
//     isOpen.value = !isOpen.value;
//     return toggleModal;
// };
// const createToggle = () => {
//     alert( 'You toggled create modal' );
//     // createOpen.value = !createOpen.value;
//     isModalVisible.value = !isModalVisible.value;
//     return createToggle;
// };
// const singleToggle = () => {
//     alert( 'You toggled single modal' );
//     singleTicketOpen.value = !singleTicketOpen.value;
// };
</script>


<script>
    const searchTerm = ref('');
    
    // const filteredTableData = ref([])
    export default {
        name: 'DashBoard',
        components: {
            CreateEditTicket,
            DashBoard_Table_Row,
            SingleTicket,
            TicketModal
        },
        data () {
            return {
                modalData: null,
                singleTicketVisable: false,
                createVisable: false,
                editVisable: false,
                tableData: tickets,
                filteredTableData: tickets,
                rowsPerPage: 5,
                currentPage: 1,
                dummyData:{
                    id: null,
                    title: null,
                    description: null,
                    start_date: null,
                    completed_date: null,
                    status_id: null,
                    creator: {
                        id: null,
                        username: null,
                        email: null,
                    },
                    assigned_user: {
                        id: null,
                        username: null,
                        email: null,
                    }, 
                    created_date: null,
                    last_update: null
                }
            };
        },
        computed: {
            totalRows() {
                if(searchTerm.value != '') {
                    console.log(this.filteredTableData.length);
                    return this.filteredTableData.length;
                } else {
                    return this.tableData.length;
                }
            },

            totalPages() {
                return Math.ceil(this.totalRows / this.rowsPerPage);
            },

            currentPageData() {
                console.log(searchTerm)
                if (searchTerm.value != ''){
                    this.filterTableData
                    const startIndex = (this.currentPage - 1) * this.rowsPerPage;
                    const endIndex = startIndex + this.rowsPerPage;
                    return this.filteredTableData.slice(startIndex, endIndex);

                } else {
                    const startIndex = (this.currentPage - 1) * this.rowsPerPage;
                    const endIndex = startIndex + this.rowsPerPage;
                    return this.tableData.slice(startIndex, endIndex);

                }
            },

            filterTableData() {
                console.log('filtering')
                let filteredTableData = [];
                    for(let i = 0; i < this.tableData.length; i++) {
                        if (this.tableData[i].id.includes(searchTerm.value) || this.tableData[i].title.includes(searchTerm.value) || this.tableData[i].assigned_user.username.includes(searchTerm.value) || this.tableData[i].created_date.includes(searchTerm.value)) {
                            filteredTableData.push(this.tableData[i]);
                        }
                    }

                    const startIndex = (this.currentPage - 1) * this.rowsPerPage;
                    // const endIndex = startIndex + this.rowsPerPage;
                    this.filteredTableData = filteredTableData;
                    // return filteredTableData;
            }
        },
        methods: {
            showModal(modalType, ticketData) {
                // alert( 'You opened the modal from dashboard' );
                // clicking to open closes other refs
                switch(modalType) {
                    case 'createTicket':
                        console.log('Opening Create ticket modal!');
                        this.createVisable = true;
                        this.singleTicketVisable = false;
                        this.editVisable = false;
                        break;
                    case 'singleTicket':
                        console.log("Opening single ticket modal!");
                        this.modalData = ticketData;
                        this.singleTicketVisable = true;
                        this.createVisable = false;
                        this.editVisable = false;
                        break;
                    case 'editTicket':
                        console.log('Opening Edit ticket modal!');
                        this.modalData = ticketData;
                        this.editVisable = true;
                        this.createVisable = false;
                        this.singleTicketVisable = false;
                        break;
                    }
            },
            closeModal(modalType) {
                switch(modalType) {
                    case 'createTicket':
                        console.log('Closing Create ticket modal!');
                        this.createVisable = false;
                        break;
                    case 'singleTicket':
                        console.log("Closing single ticket modal!");
                        this.singleTicketVisable = false;
                        break;
                    case 'editTicket':
                        console.log('Closing Edit ticket modal!');
                        this.editVisable = false;
                        break;
                    }
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
    <!--### ADDED ###-->
    <div  >
        <button @click="showModal('createTicket')" class="btn btn-primary">Create Ticket</button>
        <!-- <teleport to="body">
            <div class="modal" v-if="singleTicketVisable">
                note: change onclikc to on close so form input can be clocked without closing modal -->
                <!-- <CreateEditTicket
                    @close="createToggle"
                    title="Create / Edit Ticket"
                    
                /> -->
                <!-- :ticket="modalData"  
            </div>
        </teleport> #}-->
    </div>
        <!-- 
        <button @click="toggleModal" class="btn btn-warning">Test Modal</button>
        <teleport to="body">
            <div class="modal" v-if="isOpen">
                <TicketModal
                    @click="toggleModal"
                    title="Does this work?"
                    msg="I hope so"
                />
            </div>
        </teleport>
    </div> -->
    <div class="dashboard">
        <div class="dashboard-header">
            <div>
                <button class="btn btn-outline-primary">All</button>
                <button class="btn btn-primary">Mine</button>
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
                    <th>
                        <h2>Actions</h2>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, index) in currentPageData" :key="index" class="ticket-data" 
                    @click="showModal('singleTicket', row)">
                    <DashBoard_Table_Row :ticketData="row"/>
                    
                    <!--test vue bootstrap
                    <div>
                        <b-button v-b-modal.modal-1>Test BS Launch</b-button >
                        <b-modal id="modal-1" title="new ticket">
                            <SingleTicket 
                                @close="singleToggle"
                                title="Single Ticket"
                            />
                        </b-modal>
                    </div>-->
                    


                    <!-- <button @click="singleToggle" class="btn btn-success">View Ticket</button>
                    <teleport to="body">
                        <div class="modal" v-if="singleTicketOpen">
                            <SingleTicket 
                                @close="closeModal"
                                title="Single Ticket"
                            />
                        </div>
                    </teleport> -->
                </tr>
            </tbody>
            
        </table>

        
        <nav>
            <div class="pagination">
                <button @click="prevPage" :class="{ disabled: currentPage === 1 }">Previous</button>
                <button v-for="pageNumber in totalPages"
                    :key="pageNumber"
                    @click="gotoPage(pageNumber)"
                    :class="{ active: currentPage === pageNumber }">
                {{ pageNumber }}
                </button>
                <button @click="nextPage" :class="{ disabled: currentPage === totalPages }">Next</button>
            </div>
        </nav>
    </div>
        <!-- Opens Edit Ticket Component -->
        <CreateEditTicket
            v-if="editVisable"
            @close="closeModal('editTicket')"
            class="modal-popup"
            :ticketData="modalData"
        /> 
        <!-- Opens Create Ticket Component -->
        <CreateEditTicket
            v-if="createVisable"
            @close="closeModal('createTicket')"
            class="modal-popup"
            :ticketData="dummyData"
        /> 
        <!--edit ticket to close modal and open edit modal-->
        <SingleTicket v-if="singleTicketVisable" @close="closeModal('singleTicket')" :ticketData="modalData" :openEditTicket="showModal"/>
        <!--<CreateEditTicket
            v-show="singleTicketVisable"
            @click="toggleModal"
        />-->
    </template>

<style>
    @import './DashBoard.css';
    /* @import 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css';
    @import 'https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css'; */
</style>