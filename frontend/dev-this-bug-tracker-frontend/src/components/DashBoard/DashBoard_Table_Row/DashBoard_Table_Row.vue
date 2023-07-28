<script>
export default {
    props: {
        ticketData: Object
    }
}
</script>


<template>
    <td>{{ ticketData.id }}</td>
    <td>{{ ticketData.title }}</td>
    <td>{{ ticketData.creator.username }}</td>
    <td>{{ ticketData.status_id }}</td>
    <td>{{ ticketData.created_date }}</td>
    {{ console.log(ticketData) }}
    <!-- <td>{{ user.username }}</td> -->
</template>


