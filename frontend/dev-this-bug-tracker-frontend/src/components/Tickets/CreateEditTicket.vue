<script setup>
    import { ref } from 'vue';
    
    const title = ref('Title')
    const description = ref('Description')
    const storyPoints = ref('Story Points')
    const ticketStatus = ref('Open')
    const groups = ref('Groups')
    const assignedUser = ref('Assigned User')
    const parentLinks = ref('Parent Links')
    const ticketTags = ref('Ticket Tags')
    const ticketComments = ref('Ticket Comments')
</script>

<template>
    {# entire form will require prepopulate of data from database upon edit function #}
    <form action="">
        <div>
            {# minimum required #}
            <label for="">Title</label>
            {# enter values for editing form #}
            <input v-model="title"/> {{ Title }}
            <label for="">Description</label>
            {# enter values for editing form #}
            <input v-model="description"/> {{ description }}
            <label for="">Story Points / Content</label>
            {# enter values for editing form #}
            <input/>
        </div>
        <div>
            <label for="">Ticket Status</label>
            {# stored ticket status from db? #}
            <select >
                <option>Open</option>
                <option>In Progress</option>
                <option>Blocked</option>
                <option>Need More Info</option>
                <option>Closed</option>
                <option>Cancelled</option>
            </select>
            <label for="">Groups</label>
            <radio>
                {# call groups from database here #}
                <option></option>
            </radio>
            <label for="">Assigned User</label>
            <radio>
                {# call users from database here #}
                <option></option>
            </radio>
            <label for="">Parent Links</label>
            {# link parent tickets with relationship in database #}
            <ul>
                <li></li>
            </ul>
            <label for="">Ticket Tags</label>
            {# call ticket labels from database #}
            <ul>
                <li></li>
            </ul>
            <label for="">Ticket Comments</label>
            {# call ticket comments from database #}
            <textarea name="" id="" cols="30" rows="10"></textarea>
            <div>
                <button type="submit">Submit / Update</button>
            </div>
        </div>
    </form>

</template>