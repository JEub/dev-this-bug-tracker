<script>
export default {
    props: {
        ticketData: Object
    }
}
</script>


<template>
    <tr>
        <td>{{ ticketData.title }}</td>
        {{ console.log(ticketData) }}
        <!-- <td>{{ user.username }}</td> -->
    </tr>
</template>


