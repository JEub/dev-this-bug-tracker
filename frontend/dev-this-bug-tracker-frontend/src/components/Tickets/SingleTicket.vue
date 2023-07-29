<script setup>
    import { ref } from 'vue';
    
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

<template>
    <!-- pull data from database -->
    <div>
        <p>ticket id</p>
        <p>creator contact email</p>
        <p>Assigned users</p>
        <p>ticket status</p>
    </div>
    <div>
        <div>
            <p>date opened / closed</p>
        </div>
        <div>
            <p>title</p>
            <p>Description</p>
        </div>
        <div>Groups</div>
        <div>Story points</div>
        <div>
            <ul>
                <li>parent ticket links</li>
            </ul>
        </div>
        <div>
            <ul>
                <li>History of assigned users w/time worked on ticket</li>
            </ul>
        </div>
        <div>
            <p>Ticket tags</p>
        </div>
        <div>
            <p>Ticket comments</p>
        </div>
        <div>
            <!-- both of these buttons could open new modal? -->
            <button><a href="">Add Comment</a></button>
            <button><a href="">Edit Ticket</a></button>
        </div>
    </div>
</template>