<script setup>
    import { ref, reactive, onMounted, computed } from 'vue';
    import tickets from './tickets.json';
    import CreateEditTicket from '../Tickets/CreateEditTicket.vue';
    import SingleTicket from '../Tickets/SingleTicket.vue';
    import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';
    import CreateEditUser from '../Users/CreateEditUser.vue';
    import UserProfile from '../Users/UserProfile.vue';

    const modalData = ref();
    const searchTerm = ref('');
    const singleTicketVisable = ref(false);
    const createVisable = ref(false);
    const editVisable = ref(false);
    const userFormVisable = ref(false);
    const userProfileVisable = ref(false);
    const tableData = ref(tickets);
    const filteredTableData = ref(tickets);
    const rowsPerPage = 5;
    const currentPage = ref(1);
    const maxPaginationButtons = 5;
    const currentPageDisplayData = ref();
    const paginationRange = ref({
        maxLeft : 1,
        maxRight : 5
    })
    const dummyData = {
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

    function totalRows() {
        if(searchTerm.value != '') {
            return filteredTableData.value.length;
        } else {
            return tableData.value.length;
        }
    };
            
    function totalPages() {
        return Math.ceil(totalRows() / rowsPerPage);
    };
    
    const currentPageDataInfo = computed(() => {
        console.log(currentPage.value)
        // paginationButton();
        // filterTableData();
        const startIndex = (currentPage.value - 1) * rowsPerPage;
        const endIndex = startIndex + rowsPerPage;
        console.log('Start Index, ', startIndex)
        console.log('End Index, ', endIndex)
        console.log(filteredTableData.value.slice(startIndex, endIndex))
        return filteredTableData.value.slice(startIndex, endIndex);
        
    })
    // function currentPageData() {
    //     console.log(currentPage.value)
    //     // paginationButton();
    //     // filterTableData();
    //     const startIndex = (currentPage.value - 1) * rowsPerPage;
    //     const endIndex = startIndex + rowsPerPage;
    //     console.log('Start Index, ', startIndex)
    //     console.log('End Index, ', endIndex)
    //     console.log(filteredTableData.value.slice(startIndex, endIndex))
    //     return filteredTableData.value.slice(startIndex, endIndex);
        
    // };

    function filterTableData() {
        console.log('Calling Filter Table Data Function')
        let tempFilteredTableData = [];
        currentPage.value = 1;
        for(let i = 0; i < tableData.value.length; i++) {
            // can this all be condensed to switch case or create additional if statements?
            if (
                tableData.value[i].id.includes(searchTerm.value) || 
                tableData.value[i].title.includes(searchTerm.value) || 
                tableData.value[i].assigned_user.username.includes(searchTerm.value) || 
                tableData.value[i].created_date.includes(searchTerm.value)) {
                    tempFilteredTableData.push(tableData.value[i]);
                }
        }
        filteredTableData.value = tempFilteredTableData;
    }
    

    function showModal(modalType, ticketData) {
        switch(modalType) {
            case 'createTicket':
                // console.log('Opening Create ticket modal!');
                createVisable.value = true;
                singleTicketVisable.value = false;
                editVisable.value = false;
                break;
            case 'singleTicket':
                // console.log("Opening single ticket modal!");
                modalData.value = ticketData;
                singleTicketVisable.value = true;
                createVisable.value = false;
                editVisable.value = false;
                break;
            case 'editTicket':
                // console.log('Opening Edit ticket modal!');
                modalData.value = ticketData;
                editVisable.value = true;
                createVisable.value = false;
                singleTicketVisable.value = false;
                break;
            case 'userForm':
                // console.log('Opening User Form modal!');
                // this.modalData = ticketData;
                userFormVisable.value = true;
                userProfileVisable.value = false;
                break;
            case 'userProfile':
                // console.log('Opening User Profile modal!');
                // this.modalData = userData;
                userProfileVisable.value = true;
                userFormVisable.value = false;
                break;
        }
                    
    }
            // CLOSE MODAL WITH ARGUEMENT
    function closeModal(modalType) {
        switch(modalType) {
            case 'createTicket':
                // console.log('Closing Create ticket modal!');
                createVisable.value = false;
                break;
            case 'singleTicket':
                // console.log("Closing single ticket modal!");
                singleTicketVisable.value = false;
                break;
            case 'editTicket':
                // console.log('Closing Edit ticket modal!');
                editVisable.value = false;
                break;
            case 'userForm':
                // console.log('Opening User Form modal!');
                // this.modalData = ticketData;
                userFormVisable.value = false;
            case 'userProfile':
                // console.log('Closing User Profile modal!');
                // this.modalData = userData;
                userProfileVisable.value = false;
                break;
        }
    }
            // PAGINATION
    function paginationButton() {
        console.log('Calling Pagination Buttons Function');
        // console.log(currentPage.value - Math.floor(maxPaginationButtons /2))
        let maxLeft = (currentPage.value - Math.floor(maxPaginationButtons /2));
        let maxRight = (currentPage.value + Math.floor(maxPaginationButtons /2));
        // console.log(maxLeft)
        // console.log(maxRight)
        if (maxLeft < 1) {
            // console.log('test one')
            maxLeft = 1;
            maxRight = maxPaginationButtons
            // console.log(maxLeft)
            // console.log(maxRight)
        }
        console.log(maxRight > totalPages())
        console.log('test 2')
        if (maxRight > totalPages()) {
            console.log('test 3')
            maxLeft = totalPages() - (maxPaginationButtons - 1);
            maxRight = totalPages()
            if (maxLeft < 1) {
                console.log('test four')
                maxLeft = 1;
            }
        }
        paginationRange.value = {
            maxLeft: maxLeft,
            maxRight: maxRight
        }
        console.log(paginationRange.value)
    }

    function range(start, end) {
        return Array.from({ length: end - start + 1 }, (_, index) => start + index);
    }

    function prevPage() {
        if(currentPage.value > 1) {
            console.log(currentPage.value)
            currentPage.value--;
            console.log(currentPage.value)
            paginationButton()
            currentPageDataInfo
            // currentPageDisplayData.value = currentPageData();
        }
    }

    function nextPage() {
        if (currentPage.value < totalPages()) {
            console.log(currentPage.value)
            currentPage.value++;
            console.log(currentPage.value)
            paginationButton()
            currentPageDataInfo
            // currentPageDisplayData.value = currentPageData();
        }
    }
            
    function gotoPage(pageNumber) {
        // console.log(currentPage.value)
        // currentPageDisplayData.value = currentPageData();
        console.log(currentPage.value)
        currentPage.value = pageNumber;
        console.log(currentPage.value)
        paginationButton()
        currentPageDataInfo
    }

    // CLOSE MODAL
    function close() {
    // uses Options API to emit a custom event
        this.$emit('close');
    }
        
    //Temp Function
    
              
    // onMounted(() => 
    //     currentPageDisplayData.value = currentPageDataInfo,
    //     console.log(currentPageDataInfo)
    // )

    
</script>

<template>
    <div id="container">
        <div id="nav">
            <h2>Welcome, User</h2>
            <div>
                <img src="../../assets/userProfile.svg"/> 
                <a>Logout</a>
            </div>
            <button @click="showModal('createTicket')" class="btn btn-primary">Create Ticket</button>
            <button @click="showModal('userForm')" class="btn btn-outline-secondary">Create User</button>
            <button @click="showModal('userProfile')"
            class="btn btn-outline-success"
            >Profile</button>
        </div>
        <div class="dashboard">
            <div class="dashboard-header">
                <div >
                    <!--Add filter option here for user specific settings; groups, ticket status queues, assigned to user-->
                    <button class="btn btn-outline-primary">All</button>
                    <button class="btn btn-primary">Mine</button>
                </div>
                <div>
                    <input type='text' placeholder="Search" v-model="searchTerm"/>
                    <button>Filter</button>
                </div>
            </div>
            <div class="table-data-container">
                <table id="myTable" class="table table-striped table-hover dashboard-table">
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
                        <tr v-for="(row, index) in currentPageDataInfo" :key="index" class="ticket-data" 
                            @click="showModal('singleTicket', row)">
                            <DashBoard_Table_Row :ticketData="row"/>
                        </tr>
                    </tbody>
                </table>
            </div>
            <nav class="pagination-container">
                <div class="pagination">
                    <button @click="prevPage()" class="pagination-button" :class="{ disabled: currentPage === 1 }">Previous</button>
                    <button v-for="pageNumber in range(paginationRange.maxLeft, paginationRange.maxRight)"
                        :key="pageNumber"
                        @click="gotoPage(pageNumber)" 
                        :class="{ active: currentPage === pageNumber }"
                        class="pagination-button" >
                    {{ pageNumber }}
                    </button>
                    <button @click="nextPage()" class="pagination-button" :class="{ disabled: currentPage === totalPages }">Next</button>
                </div>
            </nav>
        </div>
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
        <SingleTicket v-if="singleTicketVisable" @close="closeModal('singleTicket')" :ticketData="modalData" :openEditTicket="showModal"/>
        <!--Opens User Create Modal-->
        <CreateEditUser
            v-if="userFormVisable" 
            @close="closeModal('userForm')"
            :openUserProfile="showModal"
        />
        <!--Opens user profile-->
        <UserProfile
            v-if="userProfileVisable"
            @close="closeModal('userProfile')"
            :openEditUser="showModal"
        />
    </template>

<style>
    @import './DashBoard.css';
</style>